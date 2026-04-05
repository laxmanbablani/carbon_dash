# AUTO GENERATED FILE - DO NOT EDIT

#' @export
select <- function(children=NULL, id=NULL, className=NULL, decorator=NULL, defaultValue=NULL, disabled=NULL, helperText=NULL, hideLabel=NULL, inline=NULL, invalid=NULL, invalidText=NULL, label=NULL, labelText=NULL, light=NULL, loading_state=NULL, noLabel=NULL, onChange=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, readOnly=NULL, size=NULL, slug=NULL, style=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, decorator=decorator, defaultValue=defaultValue, disabled=disabled, helperText=helperText, hideLabel=hideLabel, inline=inline, invalid=invalid, invalidText=invalidText, label=label, labelText=labelText, light=light, loading_state=loading_state, noLabel=noLabel, onChange=onChange, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, readOnly=readOnly, size=size, slug=slug, style=style, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Select',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'decorator', 'defaultValue', 'disabled', 'helperText', 'hideLabel', 'inline', 'invalid', 'invalidText', 'label', 'labelText', 'light', 'loading_state', 'noLabel', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'size', 'slug', 'style', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
