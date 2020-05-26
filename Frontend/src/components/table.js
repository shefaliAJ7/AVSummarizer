import React from 'react';

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const styles = theme => ({

  table: {
    minWidth: 700,
  },
});
String.prototype.trunc = String.prototype.trunc ||
      function(n){
          return (this.length > n) ? this.substr(0, n-1) + '...' : this;
  };


function SimpleTable(props) {
  const { data, type } = props;
  console.log(data, type);

  var l = []
  if(type == 'links' && data != null){
    for(let i = 0; i<data.length; i++){
      var s = data[i][0];
     
      var title = s.split('/')
      
      s = 'https://'+ title[2]
      l.push(<TableRow><TableCell key={i + data[i][0]}><a href={data[i][0]} target='_blank'>{s.trunc(45)}</a></TableCell>
                <TableCell key={i+ data[i][1]}>{data[i][1]}</TableCell>
          </TableRow>); //
    }

  }
  if(type=="domains") {
    return (
      <Paper >
        <Table >
          <TableHead>
            <TableRow >
              <TableCell className='headingTable'>Top Domains</TableCell>
              <TableCell className='headingTable' style={{padding: "4px 10px 4px 24px !important"}}>Count</TableCell>
             
            </TableRow>
          </TableHead>
          <TableBody>{l}</TableBody>
        </Table>
      </Paper>)
  }
  else {
     return (
       <Paper >
        <Table >
          <TableHead>
            <TableRow >
              <TableCell className='headingTable'>Top Links</TableCell>
              <TableCell className='headingTable' style={{padding: "4px 10px 4px 24px !important"}}>Count</TableCell>
           </TableRow>
          </TableHead>
          <TableBody>{l}</TableBody>
        </Table>
      </Paper>)
  }  
  
}

export default SimpleTable;
