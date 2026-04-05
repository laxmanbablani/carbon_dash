# AUTO GENERATED FILE - DO NOT EDIT

#' @export
textArea <- function(children=NULL, id=NULL, className=NULL, cols=NULL, counterMode=NULL, debounce=NULL, decorator=NULL, defaultValue=NULL, disabled=NULL, enableCounter=NULL, helperText=NULL, hideLabel=NULL, invalid=NULL, invalidText=NULL, label=NULL, labelText=NULL, light=NULL, loading_state=NULL, maxCount=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, onClick=NULL, onKeyDown=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, placeholder=NULL, readOnly=NULL, rows=NULL, slug=NULL, style=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, cols=cols, counterMode=counterMode, debounce=debounce, decorator=decorator, defaultValue=defaultValue, disabled=disabled, enableCounter=enableCounter, helperText=helperText, hideLabel=hideLabel, invalid=invalid, invalidText=invalidText, label=label, labelText=labelText, light=light, loading_state=loading_state, maxCount=maxCount, n_blur=n_blur, n_submit=n_submit, onChange=onChange, onClick=onClick, onKeyDown=onKeyDown, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, placeholder=placeholder, readOnly=readOnly, rows=rows, slug=slug, style=style, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TextArea',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'cols', 'counterMode', 'debounce', 'decorator', 'defaultValue', 'disabled', 'enableCounter', 'helperText', 'hideLabel', 'invalid', 'invalidText', 'label', 'labelText', 'light', 'loading_state', 'maxCount', 'n_blur', 'n_submit', 'onChange', 'onClick', 'onKeyDown', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'rows', 'slug', 'style', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
