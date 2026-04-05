# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fluidTimePicker <- function(children=NULL, id=NULL, className=NULL, disabled=NULL, invalid=NULL, invalidText=NULL, labelText=NULL, loading_state=NULL, readOnly=NULL, style=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, disabled=disabled, invalid=invalid, invalidText=invalidText, labelText=labelText, loading_state=loading_state, readOnly=readOnly, style=style, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FluidTimePicker',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'disabled', 'invalid', 'invalidText', 'labelText', 'loading_state', 'readOnly', 'style', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
