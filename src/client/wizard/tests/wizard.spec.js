import { shallowMount } from "@vue/test-utils";
import Wizard from "../src/components/Wizard.vue";

describe("Wizard.vue", () => {
    it('render correct', () => {
        const wrapper = shallowMount(Wizard);
        expect(wrapper.find('h1').text()).toBe('Wizard');
    });
});