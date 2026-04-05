# AUTO GENERATED FILE - DO NOT EDIT

#' @export
search <- function(children=NULL, id=NULL, autoComplete=NULL, className=NULL, closeButtonLabelText=NULL, debounce=NULL, defaultValue=NULL, disabled=NULL, isExpanded=NULL, labelText=NULL, light=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, onClear=NULL, onExpand=NULL, onKeyDown=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, placeholder=NULL, renderIcon=NULL, role=NULL, size=NULL, style=NULL, type=NULL, value=NULL) {
    
    props <- list(children=children, id=id, autoComplete=autoComplete, className=className, closeButtonLabelText=closeButtonLabelText, debounce=debounce, defaultValue=defaultValue, disabled=disabled, isExpanded=isExpanded, labelText=labelText, light=light, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, onChange=onChange, onClear=onClear, onExpand=onExpand, onKeyDown=onKeyDown, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, placeholder=placeholder, renderIcon=renderIcon, role=role, size=size, style=style, type=type, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Search',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'autoComplete', 'className', 'closeButtonLabelText', 'debounce', 'defaultValue', 'disabled', 'isExpanded', 'labelText', 'light', 'loading_state', 'n_blur', 'n_submit', 'onChange', 'onClear', 'onExpand', 'onKeyDown', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'renderIcon', 'role', 'size', 'style', 'type', 'value'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
