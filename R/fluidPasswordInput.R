# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fluidPasswordInput <- function(children=NULL, id=NULL, className=NULL, debounce=NULL, defaultValue=NULL, disabled=NULL, hidePasswordLabel=NULL, invalid=NULL, invalidText=NULL, isPassword=NULL, labelText=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, onClick=NULL, onTogglePasswordVisibility=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, placeholder=NULL, readOnly=NULL, showPasswordLabel=NULL, style=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, debounce=debounce, defaultValue=defaultValue, disabled=disabled, hidePasswordLabel=hidePasswordLabel, invalid=invalid, invalidText=invalidText, isPassword=isPassword, labelText=labelText, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, onChange=onChange, onClick=onClick, onTogglePasswordVisibility=onTogglePasswordVisibility, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, placeholder=placeholder, readOnly=readOnly, showPasswordLabel=showPasswordLabel, style=style, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FluidPasswordInput',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'debounce', 'defaultValue', 'disabled', 'hidePasswordLabel', 'invalid', 'invalidText', 'isPassword', 'labelText', 'loading_state', 'n_blur', 'n_submit', 'onChange', 'onClick', 'onTogglePasswordVisibility', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'showPasswordLabel', 'style', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
