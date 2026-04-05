# AUTO GENERATED FILE - DO NOT EDIT

#' @export
datePickerInput <- function(children=NULL, id=NULL, className=NULL, datePickerType=NULL, decorator=NULL, disabled=NULL, helperText=NULL, hideLabel=NULL, invalid=NULL, invalidText=NULL, labelText=NULL, loading_state=NULL, onChange=NULL, onClick=NULL, pattern=NULL, placeholder=NULL, readOnly=NULL, size=NULL, slug=NULL, style=NULL, type=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, datePickerType=datePickerType, decorator=decorator, disabled=disabled, helperText=helperText, hideLabel=hideLabel, invalid=invalid, invalidText=invalidText, labelText=labelText, loading_state=loading_state, onChange=onChange, onClick=onClick, pattern=pattern, placeholder=placeholder, readOnly=readOnly, size=size, slug=slug, style=style, type=type, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DatePickerInput',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'datePickerType', 'decorator', 'disabled', 'helperText', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'loading_state', 'onChange', 'onClick', 'pattern', 'placeholder', 'readOnly', 'size', 'slug', 'style', 'type', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
