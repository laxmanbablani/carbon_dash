# AUTO GENERATED FILE - DO NOT EDIT

#' @export
overflowMenu <- function(children=NULL, id=NULL, align=NULL, ariaLabel=NULL, className=NULL, direction=NULL, flipped=NULL, focusTrap=NULL, iconClass=NULL, iconDescription=NULL, left=NULL, light=NULL, loading_state=NULL, menuOffset=NULL, menuOffsetFlip=NULL, menuOptionsClass=NULL, onClick=NULL, onClose=NULL, onFocus=NULL, onKeyDown=NULL, onOpen=NULL, open=NULL, renderIcon=NULL, selectorPrimaryFocus=NULL, size=NULL, style=NULL, top=NULL) {
    
    props <- list(children=children, id=id, align=align, ariaLabel=ariaLabel, className=className, direction=direction, flipped=flipped, focusTrap=focusTrap, iconClass=iconClass, iconDescription=iconDescription, left=left, light=light, loading_state=loading_state, menuOffset=menuOffset, menuOffsetFlip=menuOffsetFlip, menuOptionsClass=menuOptionsClass, onClick=onClick, onClose=onClose, onFocus=onFocus, onKeyDown=onKeyDown, onOpen=onOpen, open=open, renderIcon=renderIcon, selectorPrimaryFocus=selectorPrimaryFocus, size=size, style=style, top=top)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'OverflowMenu',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'ariaLabel', 'className', 'direction', 'flipped', 'focusTrap', 'iconClass', 'iconDescription', 'left', 'light', 'loading_state', 'menuOffset', 'menuOffsetFlip', 'menuOptionsClass', 'onClick', 'onClose', 'onFocus', 'onKeyDown', 'onOpen', 'open', 'renderIcon', 'selectorPrimaryFocus', 'size', 'style', 'top'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
