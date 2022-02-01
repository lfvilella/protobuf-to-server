import { GHSearchRequest, GHSearchResponse } from './github_pb';

const search = (request: GHSearchRequest): Promise<GHSearchResponse> => {
    return new Promise<GHSearchResponse>((resolve, reject) => {
        const qs = new URLSearchParams(JSON.parse(JSON.stringify(request.toObject())));
        fetch(`/rest/search?${qs.toString()}`)
            .then(response => {
                if (!response.ok) {
                    const err = `API call failed: ${response.status}:${response.statusText}`;
                    throw new Error(err);
                }
                return response.json();
            })
            .then(data => {
                const response = new GHSearchResponse()
                // TODO find a scalable way for converting objt to pb
                response.setType(data.type);
                response.setServerResponse(data.serverResponse);
                return resolve(response);
            }).catch(error => {
                return reject(error);
            });
    });
}

export { search }