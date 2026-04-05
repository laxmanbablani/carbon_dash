# AUTO GENERATED FILE - DO NOT EDIT

#' @export
slider <- function(children=NULL, id=NULL, ariaLabelInput=NULL, className=NULL, debounce=NULL, disabled=NULL, formatLabel=NULL, hideLabel=NULL, hideTextInput=NULL, inputType=NULL, invalid=NULL, invalidText=NULL, label=NULL, labelText=NULL, light=NULL, loading_state=NULL, max=NULL, maxLabel=NULL, min=NULL, minLabel=NULL, n_blur=NULL, n_submit=NULL, name=NULL, onBlur=NULL, onChange=NULL, onInputKeyUp=NULL, onRelease=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, readOnly=NULL, required=NULL, step=NULL, stepMultiplier=NULL, style=NULL, translateWithId=NULL, unstable_ariaLabelInputUpper=NULL, unstable_nameUpper=NULL, unstable_valueUpper=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, ariaLabelInput=ariaLabelInput, className=className, debounce=debounce, disabled=disabled, formatLabel=formatLabel, hideLabel=hideLabel, hideTextInput=hideTextInput, inputType=inputType, invalid=invalid, invalidText=invalidText, label=label, labelText=labelText, light=light, loading_state=loading_state, max=max, maxLabel=maxLabel, min=min, minLabel=minLabel, n_blur=n_blur, n_submit=n_submit, name=name, onBlur=onBlur, onChange=onChange, onInputKeyUp=onInputKeyUp, onRelease=onRelease, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, readOnly=readOnly, required=required, step=step, stepMultiplier=stepMultiplier, style=style, translateWithId=translateWithId, unstable_ariaLabelInputUpper=unstable_ariaLabelInputUpper, unstable_nameUpper=unstable_nameUpper, unstable_valueUpper=unstable_valueUpper, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Slider',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabelInput', 'className', 'debounce', 'disabled', 'formatLabel', 'hideLabel', 'hideTextInput', 'inputType', 'invalid', 'invalidText', 'label', 'labelText', 'light', 'loading_state', 'max', 'maxLabel', 'min', 'minLabel', 'n_blur', 'n_submit', 'name', 'onBlur', 'onChange', 'onInputKeyUp', 'onRelease', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'required', 'step', 'stepMultiplier', 'style', 'translateWithId', 'unstable_ariaLabelInputUpper', 'unstable_nameUpper', 'unstable_valueUpper', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
