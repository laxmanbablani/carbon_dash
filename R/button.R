# AUTO GENERATED FILE - DO NOT EDIT

#' @export
button <- function(children=NULL, id=NULL, as_=NULL, autoAlign=NULL, className=NULL, dangerDescription=NULL, disabled=NULL, hasIconOnly=NULL, href=NULL, iconDescription=NULL, isExpressive=NULL, isSelected=NULL, kind=NULL, loading_state=NULL, n_clicks=NULL, onBlur=NULL, onClick=NULL, onFocus=NULL, onMouseEnter=NULL, onMouseLeave=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, rel=NULL, renderIcon=NULL, role=NULL, size=NULL, style=NULL, tabIndex=NULL, target=NULL, tooltipAlignment=NULL, tooltipDropShadow=NULL, tooltipHighContrast=NULL, tooltipPosition=NULL, type=NULL) {
    
    props <- list(children=children, id=id, as_=as_, autoAlign=autoAlign, className=className, dangerDescription=dangerDescription, disabled=disabled, hasIconOnly=hasIconOnly, href=href, iconDescription=iconDescription, isExpressive=isExpressive, isSelected=isSelected, kind=kind, loading_state=loading_state, n_clicks=n_clicks, onBlur=onBlur, onClick=onClick, onFocus=onFocus, onMouseEnter=onMouseEnter, onMouseLeave=onMouseLeave, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, rel=rel, renderIcon=renderIcon, role=role, size=size, style=style, tabIndex=tabIndex, target=target, tooltipAlignment=tooltipAlignment, tooltipDropShadow=tooltipDropShadow, tooltipHighContrast=tooltipHighContrast, tooltipPosition=tooltipPosition, type=type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Button',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'autoAlign', 'className', 'dangerDescription', 'disabled', 'hasIconOnly', 'href', 'iconDescription', 'isExpressive', 'isSelected', 'kind', 'loading_state', 'n_clicks', 'onBlur', 'onClick', 'onFocus', 'onMouseEnter', 'onMouseLeave', 'persisted_props', 'persistence', 'persistence_type', 'rel', 'renderIcon', 'role', 'size', 'style', 'tabIndex', 'target', 'tooltipAlignment', 'tooltipDropShadow', 'tooltipHighContrast', 'tooltipPosition', 'type'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
