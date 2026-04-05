# AUTO GENERATED FILE - DO NOT EDIT

#' @export
toggletip <- function(children=NULL, id=NULL, align=NULL, alignmentAxisOffset=NULL, as_=NULL, autoAlign=NULL, autoAlignBoundary=NULL, backgroundToken=NULL, border=NULL, caret=NULL, className=NULL, defaultOpen=NULL, dropShadow=NULL, highContrast=NULL, isTabTip=NULL, loading_state=NULL, onRequestClose=NULL, style=NULL) {
    
    props <- list(children=children, id=id, align=align, alignmentAxisOffset=alignmentAxisOffset, as_=as_, autoAlign=autoAlign, autoAlignBoundary=autoAlignBoundary, backgroundToken=backgroundToken, border=border, caret=caret, className=className, defaultOpen=defaultOpen, dropShadow=dropShadow, highContrast=highContrast, isTabTip=isTabTip, loading_state=loading_state, onRequestClose=onRequestClose, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Toggletip',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'alignmentAxisOffset', 'as_', 'autoAlign', 'autoAlignBoundary', 'backgroundToken', 'border', 'caret', 'className', 'defaultOpen', 'dropShadow', 'highContrast', 'isTabTip', 'loading_state', 'onRequestClose', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
