# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fluidSelect <- function(children=NULL, id=NULL, className=NULL, defaultValue=NULL, disabled=NULL, invalid=NULL, invalidText=NULL, labelText=NULL, loading_state=NULL, onChange=NULL, readOnly=NULL, style=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultValue=defaultValue, disabled=disabled, invalid=invalid, invalidText=invalidText, labelText=labelText, loading_state=loading_state, onChange=onChange, readOnly=readOnly, style=style, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FluidSelect',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultValue', 'disabled', 'invalid', 'invalidText', 'labelText', 'loading_state', 'onChange', 'readOnly', 'style', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
