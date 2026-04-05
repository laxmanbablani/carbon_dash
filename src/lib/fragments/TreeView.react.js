import React from 'react';
import { TreeView as CarbonTreeView } from '@carbon/react';

const TreeView = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        style,
        ...otherProps
    } = props;

    const onSelect = (event, node) => {
        if (setProps) {
            setProps({
                active: node.nodeId || node.id || node.activeNodeId,
            });
        }
    };

    return (
        <CarbonTreeView
            id={id}
            className={className}
            style={style}
            onSelect={onSelect}
            {...otherProps}
        >
            {children}
        </CarbonTreeView>
    );
};

export default TreeView;
