# AUTO GENERATED FILE - DO NOT EDIT

#' @export
timePicker <- function(children=NULL, id=NULL, className=NULL, debounce=NULL, disabled=NULL, hideLabel=NULL, invalid=NULL, invalidText=NULL, labelText=NULL, light=NULL, loading_state=NULL, maxLength=NULL, n_blur=NULL, n_submit=NULL, onBlur=NULL, onChange=NULL, onClick=NULL, pattern=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, placeholder=NULL, readOnly=NULL, size=NULL, style=NULL, type=NULL, value=NULL, warning=NULL, warningText=NULL) {
    
    props <- list(children=children, id=id, className=className, debounce=debounce, disabled=disabled, hideLabel=hideLabel, invalid=invalid, invalidText=invalidText, labelText=labelText, light=light, loading_state=loading_state, maxLength=maxLength, n_blur=n_blur, n_submit=n_submit, onBlur=onBlur, onChange=onChange, onClick=onClick, pattern=pattern, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, placeholder=placeholder, readOnly=readOnly, size=size, style=style, type=type, value=value, warning=warning, warningText=warningText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TimePicker',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'debounce', 'disabled', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'light', 'loading_state', 'maxLength', 'n_blur', 'n_submit', 'onBlur', 'onChange', 'onClick', 'pattern', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'size', 'style', 'type', 'value', 'warning', 'warningText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
