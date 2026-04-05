# AUTO GENERATED FILE - DO NOT EDIT

#' @export
iconTab <- function(children=NULL, id=NULL, badgeIndicator=NULL, className=NULL, defaultOpen=NULL, enterDelayMs=NULL, label=NULL, leaveDelayMs=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, badgeIndicator=badgeIndicator, className=className, defaultOpen=defaultOpen, enterDelayMs=enterDelayMs, label=label, leaveDelayMs=leaveDelayMs, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'IconTab',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'badgeIndicator', 'className', 'defaultOpen', 'enterDelayMs', 'label', 'leaveDelayMs', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
