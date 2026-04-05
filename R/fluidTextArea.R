# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fluidTextArea <- function(children=NULL, id=NULL, className=NULL, cols=NULL, debounce=NULL, defaultValue=NULL, disabled=NULL, enableCounter=NULL, helperText=NULL, hideLabel=NULL, invalid=NULL, invalidText=NULL, labelText=NULL, light=NULL, loading_state=NULL, maxCount=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, onClick=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, placeholder=NULL, readOnly=NULL, rows=NULL, style=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, cols=cols, debounce=debounce, defaultValue=defaultValue, disabled=disabled, enableCounter=enableCounter, helperText=helperText, hideLabel=hideLabel, invalid=invalid, invalidText=invalidText, labelText=labelText, light=light, loading_state=loading_state, maxCount=maxCount, n_blur=n_blur, n_submit=n_submit, onChange=onChange, onClick=onClick, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, placeholder=placeholder, readOnly=readOnly, rows=rows, style=style, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FluidTextArea',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'cols', 'debounce', 'defaultValue', 'disabled', 'enableCounter', 'helperText', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'light', 'loading_state', 'maxCount', 'n_blur', 'n_submit', 'onChange', 'onClick', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'rows', 'style', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
