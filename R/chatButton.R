# AUTO GENERATED FILE - DO NOT EDIT

#' @export
chatButton <- function(children=NULL, id=NULL, className=NULL, disabled=NULL, isQuickAction=NULL, isSelected=NULL, kind=NULL, loading_state=NULL, renderIcon=NULL, size=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, disabled=disabled, isQuickAction=isQuickAction, isSelected=isSelected, kind=kind, loading_state=loading_state, renderIcon=renderIcon, size=size, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ChatButton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'disabled', 'isQuickAction', 'isSelected', 'kind', 'loading_state', 'renderIcon', 'size', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
