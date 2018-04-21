import React from 'react'
import Link from 'gatsby-link'
import ReactTable from "react-table";
import 'react-table/react-table.css'


const IndexPage = () => (
  <div>
    <h1>Hi people</h1>
    <p>Welcome to your new Gatsby site.</p>
    <p>Now go build something great.</p>
    <Link to="/page-2/">Go to page 2</Link>
  </div>
)

class IndexPageC extends React.Component {

    render() {

        const jobdata = [{
            location: 'Canberra',
            title: 'Software-Dev',
            company: 'Placeholder',
            summary: 'AAAAAAAAAAAGGGGGGGGHAAAAA',
            salary: 'Nothing Found'
            }, {
             location: 'Canberra',
             title: 'Software-Dev2',
             company: 'PlaceholderA',
             summary: 'AAAAAAAAAAAGGGGGGGGHAAAAA',
             salary: 'Nothing Found'
            }
        ]

        const jobcolumns = [{
                Header: 'Location',
                accessor: 'location' // String-based value accessors!
            }, {
                Header: 'Title',
                accessor: 'title',
            }, {
                Header: 'Company',
                accessor: 'company',
            }, {
                Header: 'Summary',
                accessor: 'summary',
            }]

        return (
            

            <div>
                <h1>HELLO M8S!</h1>
                <p>Welcome to your new Gatsby site.</p>
                <p>Now go build something great.</p>
                <Link to="/page-2/">Go to page 2</Link>
                <ReactTable
                    data={jobdata}
                    columns={jobcolumns}
                    defaultPageSize={10}
                />
            </div>    

            
        )
    }

}

export default IndexPageC
