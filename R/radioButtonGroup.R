# AUTO GENERATED FILE - DO NOT EDIT

#' @export
radioButtonGroup <- function(children=NULL, id=NULL, className=NULL, decorator=NULL, defaultSelected=NULL, disabled=NULL, helperText=NULL, invalid=NULL, invalidText=NULL, label=NULL, labelPosition=NULL, legendText=NULL, loading_state=NULL, name=NULL, onChange=NULL, orientation=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, readOnly=NULL, required=NULL, slug=NULL, style=NULL, valueSelected=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, decorator=decorator, defaultSelected=defaultSelected, disabled=disabled, helperText=helperText, invalid=invalid, invalidText=invalidText, label=label, labelPosition=labelPosition, legendText=legendText, loading_state=loading_state, name=name, onChange=onChange, orientation=orientation, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, readOnly=readOnly, required=required, slug=slug, style=style, valueSelected=valueSelected, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'RadioButtonGroup',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'decorator', 'defaultSelected', 'disabled', 'helperText', 'invalid', 'invalidText', 'label', 'labelPosition', 'legendText', 'loading_state', 'name', 'onChange', 'orientation', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'required', 'slug', 'style', 'valueSelected', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
