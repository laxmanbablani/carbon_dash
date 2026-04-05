import React from 'react';
import { FileUploaderItem as CarbonFileUploaderItem } from '@carbon/react';

const FileUploaderItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFileUploaderItem
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFileUploaderItem>
    );
};



export default FileUploaderItem;
