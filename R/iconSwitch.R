# AUTO GENERATED FILE - DO NOT EDIT

#' @export
iconSwitch <- function(children=NULL, id=NULL, align=NULL, className=NULL, disabled=NULL, enterDelayMs=NULL, index=NULL, leaveDelayMs=NULL, loading_state=NULL, name=NULL, onClick=NULL, onKeyDown=NULL, selected=NULL, size=NULL, style=NULL, text=NULL) {
    
    props <- list(children=children, id=id, align=align, className=className, disabled=disabled, enterDelayMs=enterDelayMs, index=index, leaveDelayMs=leaveDelayMs, loading_state=loading_state, name=name, onClick=onClick, onKeyDown=onKeyDown, selected=selected, size=size, style=style, text=text)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'IconSwitch',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'className', 'disabled', 'enterDelayMs', 'index', 'leaveDelayMs', 'loading_state', 'name', 'onClick', 'onKeyDown', 'selected', 'size', 'style', 'text'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
