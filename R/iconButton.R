# AUTO GENERATED FILE - DO NOT EDIT

#' @export
iconButton <- function(children=NULL, id=NULL, align=NULL, autoAlign=NULL, badgeCount=NULL, className=NULL, closeOnActivation=NULL, defaultOpen=NULL, disabled=NULL, dropShadow=NULL, enterDelayMs=NULL, highContrast=NULL, href=NULL, isSelected=NULL, kind=NULL, label=NULL, leaveDelayMs=NULL, loading_state=NULL, rel=NULL, size=NULL, style=NULL, target=NULL, wrapperClasses=NULL) {
    
    props <- list(children=children, id=id, align=align, autoAlign=autoAlign, badgeCount=badgeCount, className=className, closeOnActivation=closeOnActivation, defaultOpen=defaultOpen, disabled=disabled, dropShadow=dropShadow, enterDelayMs=enterDelayMs, highContrast=highContrast, href=href, isSelected=isSelected, kind=kind, label=label, leaveDelayMs=leaveDelayMs, loading_state=loading_state, rel=rel, size=size, style=style, target=target, wrapperClasses=wrapperClasses)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'IconButton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'autoAlign', 'badgeCount', 'className', 'closeOnActivation', 'defaultOpen', 'disabled', 'dropShadow', 'enterDelayMs', 'highContrast', 'href', 'isSelected', 'kind', 'label', 'leaveDelayMs', 'loading_state', 'rel', 'size', 'style', 'target', 'wrapperClasses'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
