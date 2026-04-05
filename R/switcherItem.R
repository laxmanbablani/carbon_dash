# AUTO GENERATED FILE - DO NOT EDIT

#' @export
switcherItem <- function(children=NULL, id=NULL, className=NULL, handleSwitcherItemFocus=NULL, href=NULL, index=NULL, loading_state=NULL, onClick=NULL, onKeyDown=NULL, rel=NULL, style=NULL, tabIndex=NULL, target=NULL) {
    
    props <- list(children=children, id=id, className=className, handleSwitcherItemFocus=handleSwitcherItemFocus, href=href, index=index, loading_state=loading_state, onClick=onClick, onKeyDown=onKeyDown, rel=rel, style=style, tabIndex=tabIndex, target=target)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SwitcherItem',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'handleSwitcherItemFocus', 'href', 'index', 'loading_state', 'onClick', 'onKeyDown', 'rel', 'style', 'tabIndex', 'target'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
