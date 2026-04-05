# AUTO GENERATED FILE - DO NOT EDIT

#' @export
toggle <- function(children=NULL, id=NULL, className=NULL, defaultToggled=NULL, disabled=NULL, hideLabel=NULL, label=NULL, labelA=NULL, labelB=NULL, labelText=NULL, loading_state=NULL, onClick=NULL, onToggle=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, readOnly=NULL, size=NULL, style=NULL, toggled=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultToggled=defaultToggled, disabled=disabled, hideLabel=hideLabel, label=label, labelA=labelA, labelB=labelB, labelText=labelText, loading_state=loading_state, onClick=onClick, onToggle=onToggle, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, readOnly=readOnly, size=size, style=style, toggled=toggled)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Toggle',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultToggled', 'disabled', 'hideLabel', 'label', 'labelA', 'labelB', 'labelText', 'loading_state', 'onClick', 'onToggle', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'size', 'style', 'toggled'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
