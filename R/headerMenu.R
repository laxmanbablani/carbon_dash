# AUTO GENERATED FILE - DO NOT EDIT

#' @export
headerMenu <- function(children=NULL, id=NULL, className=NULL, focusRef=NULL, isActive=NULL, isCurrentPage=NULL, loading_state=NULL, menuLinkName=NULL, onBlur=NULL, onClick=NULL, onKeyDown=NULL, renderMenuContent=NULL, style=NULL, tabIndex=NULL) {
    
    props <- list(children=children, id=id, className=className, focusRef=focusRef, isActive=isActive, isCurrentPage=isCurrentPage, loading_state=loading_state, menuLinkName=menuLinkName, onBlur=onBlur, onClick=onClick, onKeyDown=onKeyDown, renderMenuContent=renderMenuContent, style=style, tabIndex=tabIndex)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'HeaderMenu',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'focusRef', 'isActive', 'isCurrentPage', 'loading_state', 'menuLinkName', 'onBlur', 'onClick', 'onKeyDown', 'renderMenuContent', 'style', 'tabIndex'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
