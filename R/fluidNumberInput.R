# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fluidNumberInput <- function(children=NULL, id=NULL, allowEmpty=NULL, className=NULL, debounce=NULL, defaultValue=NULL, disableWheel=NULL, disabled=NULL, formatOptions=NULL, iconDescription=NULL, inputMode=NULL, invalid=NULL, invalidText=NULL, label=NULL, loading_state=NULL, locale=NULL, max=NULL, min=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, onClick=NULL, onKeyUp=NULL, pattern=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, readOnly=NULL, step=NULL, style=NULL, translateWithId=NULL, type=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, allowEmpty=allowEmpty, className=className, debounce=debounce, defaultValue=defaultValue, disableWheel=disableWheel, disabled=disabled, formatOptions=formatOptions, iconDescription=iconDescription, inputMode=inputMode, invalid=invalid, invalidText=invalidText, label=label, loading_state=loading_state, locale=locale, max=max, min=min, n_blur=n_blur, n_submit=n_submit, onChange=onChange, onClick=onClick, onKeyUp=onKeyUp, pattern=pattern, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, readOnly=readOnly, step=step, style=style, translateWithId=translateWithId, type=type, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FluidNumberInput',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'allowEmpty', 'className', 'debounce', 'defaultValue', 'disableWheel', 'disabled', 'formatOptions', 'iconDescription', 'inputMode', 'invalid', 'invalidText', 'label', 'loading_state', 'locale', 'max', 'min', 'n_blur', 'n_submit', 'onChange', 'onClick', 'onKeyUp', 'pattern', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'step', 'style', 'translateWithId', 'type', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
