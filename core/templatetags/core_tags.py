from django import template
from django.db.models import get_model
from django.utils.encoding import smart_str

from ..models import Entry

YEAR_LIST = [2012, 2013]
FORMATTED_MONTH = {'jan': 'January', 'feb':'February', 'mar':'March', 'apr':'April',
                   'may':'May', 'jun':'June', 'jul':'July', 'aug':'August',
                   'sep':'September', 'oct':'October', 'nov':'Noember', 'dec':'December' }

register = template.Library()

def do_latest_content(parser, token):
    bits = token.split_contents()
    if len(bits) != 5:
        raise template.TemplateSyntaxError(""" 'get_latest_content'
                                            tag takes exactly four arguments""")
    model_args = bits[1].split('.')
    if len(model_args) != 2:    
        raise template.TemplateSyntaxError("""
                                First argument to'get_latest_content' must be an 
                                'application_name'.'model_name' string""")
    model = get_model(*model_args)
    if model is None:
        raise template.TemplateSyntaxError("""'get_latest_content' tag got an
                                                invalid model: %s""" % bits[1])
    return LatestContentNode(model, bits[2], bits[4])
    

class LatestContentNode(template.Node):

    def __init__(self, model, num, varname):
        self.model = model
        self.num = int(num)
        self.varname = varname
    
    def render(self,context):   
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''
        

register.tag('get_latest_content', do_latest_content)



#-------------------------------------------------------------------------------


#    This is a snippet that makes the following tag operative:
#    {% get_all_objects of model as varname that_have kwargs %} 



# Compilation function
@register.tag
def get_active_dates(parser, token):
    """
    Compiles template tag get_active_dates of ... as ... that_have ...
    """
    bits = token.contents.split(' ')
    if len(bits) < 7:
        raise template.TemplateSyntaxError(
                """ 
                get_all_objects takes exactly 6 arguments
                in a form: "
                {% get_all_objects of model as varname that_have kwargs %} "
                where model, varname and constraint are user defined
                """)
    model_args = bits[2].split('.')
    if len(model_args) != 2:
        raise template.TemplateSyntaxError("""
                                First argument to'get_all_objects' must be an 
                                'application_name'.'model_name' string""")
    model = get_model(*model_args)
    if model is None:
        raise template.TemplateSyntaxError("""django.db.models.get_model
                                            returned 'None'.  Looks like 
                                            'get_all_objects' tag got an
                                            invalid model: %s""" % bits[1])
                                            
    kwargs, varname = parse_kwargs_and_varname(parser, bits[6:])
    
    return AllObjects(model, kwargs, bits[4])
   
   
class AllObjects(template.Node):
    
    def __init__(self, model, kwargs, varname):
        self.model = model
        self.kwargs = kwargs
        self.varname = varname
    
    def render(self, context):
        
        kwargs = get_kwargs(self.kwargs, context)
        relevant_objects = self.model._default_manager.filter(**kwargs)
        relevant_data = set()
        
        if len(kwargs) == 1: 
            for object in relevant_objects:
                # month = FORMATTED_MONTH[object.month]
                relevant_data.add(object.month) 
        elif len(kwargs) == 2: 
            for object in relevant_objects:
                    relevant_data.add(object.day)
                    
        context[self.varname] = relevant_data
        return ''


def parse_kwargs_and_varname(parser, bits):
    """
    Looks through tag tokens and extracts arguments, keyword_arguments
    and variable_name to save template output.
    """
    kwargs = {}
    varname = None
    
    bits = iter(bits)
    for arg in bits:
        if arg == 'as':
            varname = bits.next()
            
        if '=' in arg:
            k, v = arg.split('=', 1)
            k = k.strip()
            kwargs[k] = parser.compile_filter(v)
        
    return  kwargs, varname

def get_kwargs(kwargs, context):
    """
    Converts arguments extracted from template into proper python form.
    """
    out_kwargs = dict([(smart_str(k,'ascii'), v.resolve(context)) 
                        for k, v in kwargs.items()])
    return  out_kwargs


# register = template.Library()
# register.tag('get_all_objects', do_all_objects)
  
## Some "docs" about compile_filter
################################################################################
"""
def compile_filter(self, token):
    "Convenient wrapper for FilterExpression"
    return FilterExpression(token, self)


And FilterExpression is documented here as:

    Parses a variable token and its optional filters (all as a single string), 
    and return a list of tuples of the filter name and arguments. Sample:

>>> token = 'variable|default:"Default value"|date:"Y-m-d"'
>>> p = Parser('')
>>> fe = FilterExpression(token, p)
>>> len(fe.filters)
2
>>> fe.var
'variable'
"""
################################################################################
# ------------------------------------------------------------------------------

# {% get_years as your_variable_name %} tag

@register.tag
def get_years(parser, token):
    """
    Compiles  the {% get_years as your_variable_name %} template tag
    """
    bits = token.split_contents()
    if len(bits) != 3:
        raise template.TemplateSyntaxError(
                """ 
                get_all_objects takes exactly 2 arguments
                in a form: "
                {% get_years as varname %} "
                where  varname is user defined
                """)
    
    return GetYears(bits[2])
 
 
class GetYears(template.Node):  
    def __init__(self, varname):
        self.varname = varname
        
    def render(self, context):
        global YEAR_LIST
        context[self.varname] = YEAR_LIST
        return ''

# register = template.Library()
# register.tag('get_years', do_get_years)





#-------------------------------------------------------------------------------


#    And This is (possibly) an improved version of  get_active_dates
#    {% i_get_active_dates of model as varname that_have kwargs %} 



# Compilation function
@register.tag
def i_get_active_dates(parser, token):
    """
    Compiles template tag i_get_active_dates of ... as ... that_have ...
    """
    bits = token.contents.split(' ')
    if len(bits) < 7:
        raise template.TemplateSyntaxError(
                """ 
                get_all_objects takes exactly 6 arguments
                in a form: "
                {% get_all_objects of model as varname that_have kwargs %} "
                where model, varname and constraint are user defined
                """)
    model_args = bits[2].split('.')
    if len(model_args) != 2:
        raise template.TemplateSyntaxError("""
                                First argument to'get_all_objects' must be an 
                                'application_name'.'model_name' string""")
    model = get_model(*model_args)
    if model is None:
        raise template.TemplateSyntaxError("""django.db.models.get_model
                                            returned 'None'.  Looks like 
                                            'get_all_objects' tag got an
                                            invalid model: %s""" % bits[1])
                                            
    kwargs, varname = parse_kwargs_and_varname(parser, bits[6:])
    
    return IAllObjects(model, kwargs, bits[4])        

class IAllObjects(template.Node):
    
    def __init__(self, model, kwargs, varname):
        self.model = model
        self.kwargs = kwargs
        self.varname = varname
    
    def render(self, context):
        
        kwargs = get_kwargs(self.kwargs, context)
        relevant_objects = self.model._default_manager.filter(**kwargs)
        relevant_data = []
        
        for object in relevant_objects:
            
            d_p = object.pub_date
            for e in relevant_data:
                if (d_p.year == e.year and d_p.month == e.month
                    and d_p.day == e.day): break
            else: 
                relevant_data.append(d_p) 
                    
        context[self.varname] = relevant_data
        return ''    
#-------------------------------------------------------------------------------  


@register.inclusion_tag("tags/section_header.html")
def section_header(header_text):
    """
    Usage: {% section_header header_text %}
    """
    return {'header_text': header_text}




    




    