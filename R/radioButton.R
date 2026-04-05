# AUTO GENERATED FILE - DO NOT EDIT

#' @export
radioButton <- function(children=NULL, id=NULL, checked=NULL, className=NULL, debounce=NULL, decorator=NULL, defaultChecked=NULL, disabled=NULL, hideLabel=NULL, invalid=NULL, invalidText=NULL, label=NULL, labelPosition=NULL, labelText=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, name=NULL, onChange=NULL, onClick=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, readOnly=NULL, required=NULL, slug=NULL, style=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, checked=checked, className=className, debounce=debounce, decorator=decorator, defaultChecked=defaultChecked, disabled=disabled, hideLabel=hideLabel, invalid=invalid, invalidText=invalidText, label=label, labelPosition=labelPosition, labelText=labelText, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, name=name, onChange=onChange, onClick=onClick, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, readOnly=readOnly, required=required, slug=slug, style=style, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'RadioButton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'checked', 'className', 'debounce', 'decorator', 'defaultChecked', 'disabled', 'hideLabel', 'invalid', 'invalidText', 'label', 'labelPosition', 'labelText', 'loading_state', 'n_blur', 'n_submit', 'name', 'onChange', 'onClick', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'required', 'slug', 'style', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
