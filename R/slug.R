# AUTO GENERATED FILE - DO NOT EDIT

#' @export
slug <- function(children=NULL, id=NULL, AILabelContent=NULL, aiText=NULL, aiTextLabel=NULL, align=NULL, alignmentAxisOffset=NULL, as_=NULL, autoAlign=NULL, autoAlignBoundary=NULL, backgroundToken=NULL, border=NULL, caret=NULL, className=NULL, defaultOpen=NULL, dropShadow=NULL, highContrast=NULL, isTabTip=NULL, kind=NULL, loading_state=NULL, onRequestClose=NULL, onRevertClick=NULL, revertActive=NULL, revertLabel=NULL, size=NULL, slugLabel=NULL, style=NULL, textLabel=NULL) {
    
    props <- list(children=children, id=id, AILabelContent=AILabelContent, aiText=aiText, aiTextLabel=aiTextLabel, align=align, alignmentAxisOffset=alignmentAxisOffset, as_=as_, autoAlign=autoAlign, autoAlignBoundary=autoAlignBoundary, backgroundToken=backgroundToken, border=border, caret=caret, className=className, defaultOpen=defaultOpen, dropShadow=dropShadow, highContrast=highContrast, isTabTip=isTabTip, kind=kind, loading_state=loading_state, onRequestClose=onRequestClose, onRevertClick=onRevertClick, revertActive=revertActive, revertLabel=revertLabel, size=size, slugLabel=slugLabel, style=style, textLabel=textLabel)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Slug',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'AILabelContent', 'aiText', 'aiTextLabel', 'align', 'alignmentAxisOffset', 'as_', 'autoAlign', 'autoAlignBoundary', 'backgroundToken', 'border', 'caret', 'className', 'defaultOpen', 'dropShadow', 'highContrast', 'isTabTip', 'kind', 'loading_state', 'onRequestClose', 'onRevertClick', 'revertActive', 'revertLabel', 'size', 'slugLabel', 'style', 'textLabel'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
