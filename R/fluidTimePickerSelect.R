# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fluidTimePickerSelect <- function(children=NULL, id=NULL, className=NULL, defaultValue=NULL, disabled=NULL, labelText=NULL, loading_state=NULL, onChange=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultValue=defaultValue, disabled=disabled, labelText=labelText, loading_state=loading_state, onChange=onChange, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FluidTimePickerSelect',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultValue', 'disabled', 'labelText', 'loading_state', 'onChange', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
