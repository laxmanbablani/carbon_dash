# AUTO GENERATED FILE - DO NOT EDIT

#' @export
notificationButton <- function(children=NULL, id=NULL, ariaLabel=NULL, className=NULL, loading_state=NULL, name=NULL, notificationType=NULL, renderIcon=NULL, style=NULL, type=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, className=className, loading_state=loading_state, name=name, notificationType=notificationType, renderIcon=renderIcon, style=style, type=type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'NotificationButton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'className', 'loading_state', 'name', 'notificationType', 'renderIcon', 'style', 'type'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
