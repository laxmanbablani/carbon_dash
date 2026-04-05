# AUTO GENERATED FILE - DO NOT EDIT

#' @export
passwordInput <- function(children=NULL, id=NULL, className=NULL, debounce=NULL, defaultValue=NULL, disabled=NULL, helperText=NULL, hideLabel=NULL, hidePasswordLabel=NULL, inline=NULL, invalid=NULL, invalidText=NULL, labelText=NULL, light=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, onClick=NULL, onTogglePasswordVisibility=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, placeholder=NULL, readOnly=NULL, showPasswordLabel=NULL, size=NULL, style=NULL, tooltipAlignment=NULL, tooltipPosition=NULL, type=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, debounce=debounce, defaultValue=defaultValue, disabled=disabled, helperText=helperText, hideLabel=hideLabel, hidePasswordLabel=hidePasswordLabel, inline=inline, invalid=invalid, invalidText=invalidText, labelText=labelText, light=light, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, onChange=onChange, onClick=onClick, onTogglePasswordVisibility=onTogglePasswordVisibility, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, placeholder=placeholder, readOnly=readOnly, showPasswordLabel=showPasswordLabel, size=size, style=style, tooltipAlignment=tooltipAlignment, tooltipPosition=tooltipPosition, type=type, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'PasswordInput',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'debounce', 'defaultValue', 'disabled', 'helperText', 'hideLabel', 'hidePasswordLabel', 'inline', 'invalid', 'invalidText', 'labelText', 'light', 'loading_state', 'n_blur', 'n_submit', 'onChange', 'onClick', 'onTogglePasswordVisibility', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'showPasswordLabel', 'size', 'style', 'tooltipAlignment', 'tooltipPosition', 'type', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
