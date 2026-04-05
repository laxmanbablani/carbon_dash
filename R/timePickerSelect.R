# AUTO GENERATED FILE - DO NOT EDIT

#' @export
timePickerSelect <- function(children=NULL, id=NULL, className=NULL, defaultValue=NULL, disabled=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultValue=defaultValue, disabled=disabled, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TimePickerSelect',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultValue', 'disabled', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
