# AUTO GENERATED FILE - DO NOT EDIT

#' @export
overflowMenuItem <- function(children=NULL, id=NULL, className=NULL, closeMenu=NULL, dangerDescription=NULL, disabled=NULL, handleOverflowMenuItemFocus=NULL, hasDivider=NULL, href=NULL, index=NULL, isDelete=NULL, itemText=NULL, loading_state=NULL, onBlur=NULL, onClick=NULL, onFocus=NULL, onKeyDown=NULL, onKeyUp=NULL, onMouseDown=NULL, onMouseEnter=NULL, onMouseLeave=NULL, onMouseUp=NULL, requireTitle=NULL, style=NULL, title=NULL, wrapperClassName=NULL) {
    
    props <- list(children=children, id=id, className=className, closeMenu=closeMenu, dangerDescription=dangerDescription, disabled=disabled, handleOverflowMenuItemFocus=handleOverflowMenuItemFocus, hasDivider=hasDivider, href=href, index=index, isDelete=isDelete, itemText=itemText, loading_state=loading_state, onBlur=onBlur, onClick=onClick, onFocus=onFocus, onKeyDown=onKeyDown, onKeyUp=onKeyUp, onMouseDown=onMouseDown, onMouseEnter=onMouseEnter, onMouseLeave=onMouseLeave, onMouseUp=onMouseUp, requireTitle=requireTitle, style=style, title=title, wrapperClassName=wrapperClassName)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'OverflowMenuItem',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'closeMenu', 'dangerDescription', 'disabled', 'handleOverflowMenuItemFocus', 'hasDivider', 'href', 'index', 'isDelete', 'itemText', 'loading_state', 'onBlur', 'onClick', 'onFocus', 'onKeyDown', 'onKeyUp', 'onMouseDown', 'onMouseEnter', 'onMouseLeave', 'onMouseUp', 'requireTitle', 'style', 'title', 'wrapperClassName'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
