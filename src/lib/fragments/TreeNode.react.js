import React from 'react';
import { TreeNode as CarbonTreeNode } from '@carbon/react';

const TreeNode = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTreeNode
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTreeNode>
    );
};



export default TreeNode;
