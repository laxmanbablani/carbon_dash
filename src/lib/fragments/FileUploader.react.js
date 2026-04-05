import React from 'react';
import { FileUploader as CarbonFileUploader } from '@carbon/react';

const FileUploader = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFileUploader
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFileUploader>
    );
};



export default FileUploader;
