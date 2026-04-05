# AUTO GENERATED FILE - DO NOT EDIT

#' @export
popover <- function(children=NULL, id=NULL, align=NULL, alignmentAxisOffset=NULL, as_=NULL, autoAlign=NULL, autoAlignBoundary=NULL, backgroundToken=NULL, border=NULL, caret=NULL, className=NULL, dropShadow=NULL, height=NULL, highContrast=NULL, isTabTip=NULL, loading_state=NULL, onRequestClose=NULL, open=NULL, style=NULL, width=NULL, x=NULL, y=NULL) {
    
    props <- list(children=children, id=id, align=align, alignmentAxisOffset=alignmentAxisOffset, as_=as_, autoAlign=autoAlign, autoAlignBoundary=autoAlignBoundary, backgroundToken=backgroundToken, border=border, caret=caret, className=className, dropShadow=dropShadow, height=height, highContrast=highContrast, isTabTip=isTabTip, loading_state=loading_state, onRequestClose=onRequestClose, open=open, style=style, width=width, x=x, y=y)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Popover',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'alignmentAxisOffset', 'as_', 'autoAlign', 'autoAlignBoundary', 'backgroundToken', 'border', 'caret', 'className', 'dropShadow', 'height', 'highContrast', 'isTabTip', 'loading_state', 'onRequestClose', 'open', 'style', 'width', 'x', 'y'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
