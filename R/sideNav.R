# AUTO GENERATED FILE - DO NOT EDIT

#' @export
sideNav <- function(children=NULL, id=NULL, addFocusListeners=NULL, addMouseListeners=NULL, className=NULL, defaultExpanded=NULL, enterDelayMs=NULL, expanded=NULL, href=NULL, isChildOfHeader=NULL, isFixedNav=NULL, isPersistent=NULL, isRail=NULL, loading_state=NULL, onOverlayClick=NULL, onSideNavBlur=NULL, onToggle=NULL, style=NULL) {
    
    props <- list(children=children, id=id, addFocusListeners=addFocusListeners, addMouseListeners=addMouseListeners, className=className, defaultExpanded=defaultExpanded, enterDelayMs=enterDelayMs, expanded=expanded, href=href, isChildOfHeader=isChildOfHeader, isFixedNav=isFixedNav, isPersistent=isPersistent, isRail=isRail, loading_state=loading_state, onOverlayClick=onOverlayClick, onSideNavBlur=onSideNavBlur, onToggle=onToggle, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SideNav',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'addFocusListeners', 'addMouseListeners', 'className', 'defaultExpanded', 'enterDelayMs', 'expanded', 'href', 'isChildOfHeader', 'isFixedNav', 'isPersistent', 'isRail', 'loading_state', 'onOverlayClick', 'onSideNavBlur', 'onToggle', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
