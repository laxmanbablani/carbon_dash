# AUTO GENERATED FILE - DO NOT EDIT

#' @export
textInput <- function(children=NULL, id=NULL, ai_label=NULL, className=NULL, debounce=NULL, decorator=NULL, defaultValue=NULL, disabled=NULL, enableCounter=NULL, helperText=NULL, hideLabel=NULL, inline=NULL, invalid=NULL, invalidText=NULL, label=NULL, labelText=NULL, light=NULL, loading_state=NULL, maxCount=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, onClick=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, placeholder=NULL, readOnly=NULL, size=NULL, slug=NULL, style=NULL, type=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, ai_label=ai_label, className=className, debounce=debounce, decorator=decorator, defaultValue=defaultValue, disabled=disabled, enableCounter=enableCounter, helperText=helperText, hideLabel=hideLabel, inline=inline, invalid=invalid, invalidText=invalidText, label=label, labelText=labelText, light=light, loading_state=loading_state, maxCount=maxCount, n_blur=n_blur, n_submit=n_submit, onChange=onChange, onClick=onClick, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, placeholder=placeholder, readOnly=readOnly, size=size, slug=slug, style=style, type=type, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TextInput',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ai_label', 'className', 'debounce', 'decorator', 'defaultValue', 'disabled', 'enableCounter', 'helperText', 'hideLabel', 'inline', 'invalid', 'invalidText', 'label', 'labelText', 'light', 'loading_state', 'maxCount', 'n_blur', 'n_submit', 'onChange', 'onClick', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'size', 'slug', 'style', 'type', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
