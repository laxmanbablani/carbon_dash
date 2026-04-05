# AUTO GENERATED FILE - DO NOT EDIT

#' @export
checkbox <- function(children=NULL, id=NULL, checked=NULL, className=NULL, debounce=NULL, decorator=NULL, defaultChecked=NULL, disabled=NULL, helperText=NULL, hideLabel=NULL, indeterminate=NULL, invalid=NULL, invalidText=NULL, label=NULL, labelText=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, readOnly=NULL, slug=NULL, style=NULL, title=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, checked=checked, className=className, debounce=debounce, decorator=decorator, defaultChecked=defaultChecked, disabled=disabled, helperText=helperText, hideLabel=hideLabel, indeterminate=indeterminate, invalid=invalid, invalidText=invalidText, label=label, labelText=labelText, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, onChange=onChange, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, readOnly=readOnly, slug=slug, style=style, title=title, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Checkbox',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'checked', 'className', 'debounce', 'decorator', 'defaultChecked', 'disabled', 'helperText', 'hideLabel', 'indeterminate', 'invalid', 'invalidText', 'label', 'labelText', 'loading_state', 'n_blur', 'n_submit', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'slug', 'style', 'title', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
