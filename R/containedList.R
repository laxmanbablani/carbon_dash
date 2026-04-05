# AUTO GENERATED FILE - DO NOT EDIT

#' @export
containedList <- function(children=NULL, id=NULL, action=NULL, className=NULL, isInset=NULL, kind=NULL, label=NULL, loading_state=NULL, size=NULL, style=NULL) {
    
    props <- list(children=children, id=id, action=action, className=className, isInset=isInset, kind=kind, label=label, loading_state=loading_state, size=size, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ContainedList',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'action', 'className', 'isInset', 'kind', 'label', 'loading_state', 'size', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
