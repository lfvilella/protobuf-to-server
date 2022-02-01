import { GithubServiceClient } from './GithubServiceClientPb';
import { GHSearchRequest, GHSearchResponse } from './github_pb';

const client = new GithubServiceClient(`//${window.location.host}`);

const search = (request: GHSearchRequest): Promise<GHSearchResponse> => {
    return new Promise<GHSearchResponse>((resolve, reject) => {

        client.search(request, {}, (err, response) => {
            if (err && err.code) {
                return reject(`API call failed: ${err.code}:${err.message}`);
            }
            return resolve(response);
        });

    });
}

export { search }