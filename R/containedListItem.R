# AUTO GENERATED FILE - DO NOT EDIT

#' @export
containedListItem <- function(children=NULL, id=NULL, action=NULL, className=NULL, disabled=NULL, loading_state=NULL, onClick=NULL, renderIcon=NULL, style=NULL) {
    
    props <- list(children=children, id=id, action=action, className=className, disabled=disabled, loading_state=loading_state, onClick=onClick, renderIcon=renderIcon, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ContainedListItem',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'action', 'className', 'disabled', 'loading_state', 'onClick', 'renderIcon', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
