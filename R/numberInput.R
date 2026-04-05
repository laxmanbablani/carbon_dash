# AUTO GENERATED FILE - DO NOT EDIT

#' @export
numberInput <- function(children=NULL, id=NULL, allowEmpty=NULL, className=NULL, debounce=NULL, decorator=NULL, defaultValue=NULL, disableWheel=NULL, disabled=NULL, formatOptions=NULL, helperText=NULL, hideLabel=NULL, hideSteppers=NULL, iconDescription=NULL, inputMode=NULL, invalid=NULL, invalidText=NULL, label=NULL, light=NULL, loading_state=NULL, locale=NULL, max=NULL, min=NULL, n_blur=NULL, n_submit=NULL, onBlur=NULL, onChange=NULL, onClick=NULL, onKeyUp=NULL, onStepperBlur=NULL, pattern=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, readOnly=NULL, size=NULL, slug=NULL, step=NULL, stepStartValue=NULL, style=NULL, translateWithId=NULL, type=NULL, validate=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, allowEmpty=allowEmpty, className=className, debounce=debounce, decorator=decorator, defaultValue=defaultValue, disableWheel=disableWheel, disabled=disabled, formatOptions=formatOptions, helperText=helperText, hideLabel=hideLabel, hideSteppers=hideSteppers, iconDescription=iconDescription, inputMode=inputMode, invalid=invalid, invalidText=invalidText, label=label, light=light, loading_state=loading_state, locale=locale, max=max, min=min, n_blur=n_blur, n_submit=n_submit, onBlur=onBlur, onChange=onChange, onClick=onClick, onKeyUp=onKeyUp, onStepperBlur=onStepperBlur, pattern=pattern, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, readOnly=readOnly, size=size, slug=slug, step=step, stepStartValue=stepStartValue, style=style, translateWithId=translateWithId, type=type, validate=validate, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'NumberInput',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'allowEmpty', 'className', 'debounce', 'decorator', 'defaultValue', 'disableWheel', 'disabled', 'formatOptions', 'helperText', 'hideLabel', 'hideSteppers', 'iconDescription', 'inputMode', 'invalid', 'invalidText', 'label', 'light', 'loading_state', 'locale', 'max', 'min', 'n_blur', 'n_submit', 'onBlur', 'onChange', 'onClick', 'onKeyUp', 'onStepperBlur', 'pattern', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'size', 'slug', 'step', 'stepStartValue', 'style', 'translateWithId', 'type', 'validate', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
