# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fluidTextInput <- function(children=NULL, id=NULL, className=NULL, debounce=NULL, defaultValue=NULL, disabled=NULL, enableCounter=NULL, invalid=NULL, invalidText=NULL, isPassword=NULL, labelText=NULL, loading_state=NULL, maxCount=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, onClick=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, placeholder=NULL, readOnly=NULL, style=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, debounce=debounce, defaultValue=defaultValue, disabled=disabled, enableCounter=enableCounter, invalid=invalid, invalidText=invalidText, isPassword=isPassword, labelText=labelText, loading_state=loading_state, maxCount=maxCount, n_blur=n_blur, n_submit=n_submit, onChange=onChange, onClick=onClick, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, placeholder=placeholder, readOnly=readOnly, style=style, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FluidTextInput',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'debounce', 'defaultValue', 'disabled', 'enableCounter', 'invalid', 'invalidText', 'isPassword', 'labelText', 'loading_state', 'maxCount', 'n_blur', 'n_submit', 'onChange', 'onClick', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'style', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
