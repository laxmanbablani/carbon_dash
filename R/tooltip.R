# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tooltip <- function(children=NULL, id=NULL, align=NULL, className=NULL, closeOnActivation=NULL, defaultOpen=NULL, description=NULL, dropShadow=NULL, enterDelayMs=NULL, highContrast=NULL, label=NULL, leaveDelayMs=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, align=align, className=className, closeOnActivation=closeOnActivation, defaultOpen=defaultOpen, description=description, dropShadow=dropShadow, enterDelayMs=enterDelayMs, highContrast=highContrast, label=label, leaveDelayMs=leaveDelayMs, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Tooltip',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'className', 'closeOnActivation', 'defaultOpen', 'description', 'dropShadow', 'enterDelayMs', 'highContrast', 'label', 'leaveDelayMs', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
