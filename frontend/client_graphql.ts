import { GHSearchRequest, GHSearchResponse } from './github_pb';

// for some reason is not generating the revesed mapping
const typeMap = Object.assign({}, GHSearchRequest.QueryType);
Object.assign(typeMap, ...Object.entries(GHSearchRequest.QueryType).map(([k, v]) => ({ [v]: k })));

const search = (request: GHSearchRequest): Promise<GHSearchResponse> => {
    return new Promise<GHSearchResponse>((resolve, reject) => {

        const variables = {
            ...request.toObject(),
            type: typeMap[request.getType()]
        };
        const query = `
        query ($query: String, $type: QueryType, $resultPerPage: Int) {
            search (
              filters: {
                query: $query,
                type: $type,
                resultPerPage: $resultPerPage
              }
            ) {
              type,
              serverResponse
          }
        }
        `
        fetch('/GraphQL', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({
                query,
                variables: variables
            })
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`API call failed: ${response.status}:${response.statusText}`);
                }
                return response.json();
            })
            .then(data => {
                if (data && data.errors) {
                    throw new Error(`API call failed: ${JSON.stringify(data)}`);
                }
                // TODO find a scalable way for converting objt to pb
                const search_data = data.data.search;
                const response = new GHSearchResponse()
                response.setType(typeMap[search_data.type] as unknown as GHSearchRequest.QueryType);
                response.setServerResponse(search_data.serverResponse);
                return resolve(response);
            }).catch(error => {
                return reject(error);
            });
    });
}

export { search }