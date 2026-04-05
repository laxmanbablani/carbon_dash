# AUTO GENERATED FILE - DO NOT EDIT

#' @export
controlledPasswordInput <- function(children=NULL, id=NULL, className=NULL, debounce=NULL, defaultValue=NULL, disabled=NULL, helperText=NULL, hideLabel=NULL, hidePasswordLabel=NULL, invalid=NULL, invalidText=NULL, labelText=NULL, light=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, onClick=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, placeholder=NULL, showPasswordLabel=NULL, size=NULL, style=NULL, tooltipAlignment=NULL, tooltipPosition=NULL, value=NULL) {
    
    props <- list(children=children, id=id, className=className, debounce=debounce, defaultValue=defaultValue, disabled=disabled, helperText=helperText, hideLabel=hideLabel, hidePasswordLabel=hidePasswordLabel, invalid=invalid, invalidText=invalidText, labelText=labelText, light=light, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, onChange=onChange, onClick=onClick, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, placeholder=placeholder, showPasswordLabel=showPasswordLabel, size=size, style=style, tooltipAlignment=tooltipAlignment, tooltipPosition=tooltipPosition, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ControlledPasswordInput',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'debounce', 'defaultValue', 'disabled', 'helperText', 'hideLabel', 'hidePasswordLabel', 'invalid', 'invalidText', 'labelText', 'light', 'loading_state', 'n_blur', 'n_submit', 'onChange', 'onClick', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'showPasswordLabel', 'size', 'style', 'tooltipAlignment', 'tooltipPosition', 'value'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
