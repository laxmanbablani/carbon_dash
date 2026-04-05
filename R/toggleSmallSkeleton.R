# AUTO GENERATED FILE - DO NOT EDIT

#' @export
toggleSmallSkeleton <- function(children=NULL, id=NULL, className=NULL, labelText=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, labelText=labelText, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ToggleSmallSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'labelText', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
