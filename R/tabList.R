# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tabList <- function(children=NULL, id=NULL, activation=NULL, className=NULL, contained=NULL, fullWidth=NULL, iconSize=NULL, leftOverflowButtonProps=NULL, light=NULL, loading_state=NULL, rightOverflowButtonProps=NULL, scrollDebounceWait=NULL, scrollIntoView=NULL, style=NULL) {
    
    props <- list(children=children, id=id, activation=activation, className=className, contained=contained, fullWidth=fullWidth, iconSize=iconSize, leftOverflowButtonProps=leftOverflowButtonProps, light=light, loading_state=loading_state, rightOverflowButtonProps=rightOverflowButtonProps, scrollDebounceWait=scrollDebounceWait, scrollIntoView=scrollIntoView, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TabList',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'activation', 'className', 'contained', 'fullWidth', 'iconSize', 'leftOverflowButtonProps', 'light', 'loading_state', 'rightOverflowButtonProps', 'scrollDebounceWait', 'scrollIntoView', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
